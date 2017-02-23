import os

#define get all sub-directories
def list_dir(dir):
    all_dirs = []
    for root, dirs, files in os.walk(dir, True):
        for name in dirs:
            cur_dir = os.path.join(root,name)
            if cur_dir.find(".svn") < 0:
                all_dirs.append(cur_dir)
    return all_dirs

#define get all source files from a directories
def join_dir_files(all_dirs):
    obj=[]
    for dir in all_dirs:
        obj += Glob(dir + '/*.cpp')
        obj += Glob(dir + '/*.cxx')
    return obj


#initial CPPPATH,CCFLAGS environment varibles
env = Environment(ENV=os.environ)
inc_flags = {'CPPPATH' : ["./"]}
env.MergeFlags(inc_flags)

cc_flags = {'CCFLAGS' : ['-D_LINUX','-pthread','-std=c++11','-D_DEBUG', '-g', '-O0']}
env.MergeFlags(cc_flags)  

#link all source files to a string
all_source_files = Glob("./*.cpp")
all_source_files += Glob("./*.cxx")

all_dirs = list_dir("./")
all_source_files += join_dir_files(all_dirs)

lib1 = File("/usr/lib64/libpthread-2.17.so")

#make a program
env.Program('ProxyServer', list(all_source_files), LIBS=[lib1],LIBPATH=["/usr/lib64/"])

