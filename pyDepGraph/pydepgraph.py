import os
import sys
import pprint


pp = pprint.PrettyPrinter()

def get_abs_path(filename):
    """
    Args:
        filename:

    Returns
        absfile file path for filename
        or None if the filepath cant be found
    """
    path_obj = os.path.abspath(filename)
    if os.path.exists(path_obj) and os.path.isfile(path_obj):
        return path_obj
    else:
        return None


def parse_include_statements(filepath):
    """
    open the file and return all the #include statments
    """
    deps = []
    with open(filepath) as file:
        data = file.readlines()

        for line in data:
            if "#include" in line:
                _ = line.strip().split(" ")[1].replace('"', '')
                deps.append(_)

    return deps


def create_node_list(data):
    pass




if __name__ == '__main__':
    src_files = [
         "sqlite/src/test_wsd.c",
         "sqlite/src/threads.c",
         "sqlite/src/tokenize.c",
         "sqlite/src/treeview.c",
         "sqlite/src/trigger.c",
         "sqlite/src/update.c",
         "sqlite/src/upsert.c",
         "sqlite/src/utf.c",
         "sqlite/src/util.c",
         "sqlite/src/vacuum.c",
         "sqlite/src/vdbe.c",
         "sqlite/src/vdbe.h",
         "sqlite/src/vdbeInt.h",
         "sqlite/src/vdbeapi.c",
         "sqlite/src/vdbeaux.c",
         "sqlite/src/vdbeblob.c",
         "sqlite/src/vdbemem.c",
         "sqlite/src/vdbesort.c",
         "sqlite/src/vdbetrace.c",
         "sqlite/src/vdbevtab.c",
         "sqlite/src/vtab.c",
         "sqlite/src/vxworks.h",
         "sqlite/src/wal.c",
         "sqlite/src/wal.h",
         "sqlite/src/walker.c",
         "sqlite/src/where.c",
         "sqlite/src/whereInt.h",
         "sqlite/src/wherecode.c",
         "sqlite/src/whereexpr.c",
         "sqlite/src/window.c"
         ]

    nodes = []
    edges = []
    collection = {}
    queue = []

    for src_file in src_files:
        src_name = os.path.basename(src_file)
        src_path = get_abs_path(src_file)
        src_deps = parse_include_statements(src_path)

        collection.update({src_name: {"filePath": src_path, "fileDeps": src_deps}})

        # update queue
        for item in src_deps:
            if item not in queue:
                queue.append(item)


    for src_file in queue:
        src_path = get_abs_path(src_file)
        print(src_path)



    # pp.pprint(collection)
    # print(len(collection))


