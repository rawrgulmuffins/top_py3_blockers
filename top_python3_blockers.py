"""
This module is used to find the projects which have the most projects waiting
for them to be ported.
"""
from collections import Counter
from pprint import pprint
import logging

import caniusepython3
from caniusepython3.dependencies import blocking_dependencies
from caniusepython3.dependencies import CircularDependencyError

def chunk_list(source_list, chunk_size):
    """
    Yield successive n-sized chunks from source.
    
    found at:
    https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
    """
    for index in range(0, len(source_list), chunk_size):
        yield source_list[index:index + chunk_size]

def write_results(top_blockers):
    with open('top_blockers', 'wt') as out_file:
        pprint(top_blockers.most_common(), stream=out_file)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    all_py_projects = list(caniusepython3.pypi.all_projects())
    py3_projects = caniusepython3.pypi.all_py3_projects()
    top_blockers = Counter()
    for py_projects_sublist in chunk_list(all_py_projects, 50):
        all_blockers = None
        try:
            all_blockers = blocking_dependencies(
                py_projects_sublist,
                py3_projects)

            blocker_list = []
            for blockers_subset in all_blockers:
                for blocker in blockers_subset:
                    blocker_list.append(blocker)
            top_blockers.update(blocker_list)
        except SyntaxError as error:
            logger.exception("{} throw on projects {}".format(
                error,
                py_projects_sublist))
        except TypeError as error:
            logger.exception("{} throw on projects {}".format(
                error,
                py_projects_sublist))
        except AttributeError as error:
            logger.exception("{} throw on projects {}".format(
                error,
                py_projects_sublist))
        except CircularDependencyError as error:
            logger.exception("{} throw on projects {}".format(
                error,
                py_projects_sublist))
        except KeyboardInterrupt:
            write_results(top_blockers)
            exit()
    write_results(top_blockers)
