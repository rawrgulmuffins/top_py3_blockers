"""
This module is used to find the projects which have the most projects waiting
for them to be ported.
"""
from collections import Counter
from pprint import pprint
import logging

import caniusepython3
from caniusepython3.dependencies import blocking_dependencies

def chunk_list(source_list, chunk_size):
    """
    Yield successive n-sized chunks from source.
    
    found at:
    https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
    """
    for index in range(0, len(source_list), chunk_size):
        yield source_list[index:index + chunk_size]

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    all_py_projects = list(caniusepython3.pypi.all_projects())
    py3_projects = caniusepython3.pypi.all_py3_projects()
    blockers_counter = Counter()
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
            blockers_counter.update(blocker_list)
        except SyntaxError as error:
            logger.error("{} throw on projects {}".format(
                error,
                py_projects_sublist))
        except TypeError as error:
            logger.error("{} throw on projects {}".format(
                error,
                py_projects_sublist))
        except AttributeError as error:
            logger.error("{} throw on projects {}".format(
                error,
                py_projects_sublist))
    pprint(blockers_counter.most_common())
