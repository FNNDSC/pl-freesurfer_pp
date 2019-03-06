#                                                            _
# freesurfer_pp ds app
#
# (c) 2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import  os
from    os          import listdir, sep
from    os.path     import abspath, basename, isdir
import  shutil
import  pudb
import  sys
import  time

# import the Chris app superclass
from chrisapp.base import ChrisApp


class Freesurfer_pp(ChrisApp):
    """
    A "dummy" app containing the output of some prior FreeSurfer runs, organized in
    
            <YR>-yr/<MO>-mo/<DA>-da
            
    directory structure within the container. This app simply copies one of these
    pre-processed output trees into the output folder of the plugin.
    
    """
    AUTHORS                 = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'FreeSurfer Pre-Populated'
    CATEGORY                = 'FreeSurfer'
    TYPE                    = 'ds'
    DESCRIPTION             = 'A "dummy" app that contains some prior FreeSurfer output and simply copies this to the output directory.'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '1.0'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT        = {}
 
    str_tree                = ''

    @staticmethod
    def dirTree_probe(dir, padding, print_files=False):
        """
        Simple method that returns a string of a dir tree layout. 

        Relies on global variable, <str_tree>!!!
        """
        Freesurfer_pp.str_tree += padding[:-1] + '+-' + basename(abspath(dir)) + '/' + '\n'
        padding = padding + ' '
        files = []
        if print_files:
            files = listdir(dir)
        else:
            files = [x for x in listdir(dir) if isdir(dir + sep + x)]
        count = 0
        for file in files:
            count += 1
            Freesurfer_pp.str_tree += padding + '|' + '\n'
            path = dir + sep + file
            if isdir(path):
                if count == len(files):
                    Freesurfer_pp.dirTree_probe(path, padding + ' ', print_files)
                else:
                    Freesurfer_pp.dirTree_probe(path, padding + '|', print_files)
            else:
                Freesurfer_pp.str_tree += padding + '+-' + file + '\n'
        return Freesurfer_pp.str_tree
    
    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """
        self.add_argument("-T", "--treePrint",
                            help        = "Simple dirtree print",
                            type        = str,
                            dest        = 'treePrint',
                            optional    = True,
                            default     = "")
        self.add_argument("-a", "--ageSpec",
                            help        = "A string in <YY>-<MM>-<DD> format that denotes an *exact* target to retrieve",
                            type        = str,
                            dest        = 'ageSpec',
                            optional    = True,
                            default     = "")
        self.add_argument("-P", "--processDelay",
                            help        = "delay timer to simulate remote processing",
                            type        = str,
                            dest        = 'processDelay',
                            optional    = True,
                            default     = "0")
        self.add_argument("-v", "--verbosity",
                            help        = "verbosity level for app",
                            type        = str,
                            dest        = 'verbosity',
                            optional    = True,
                            default     = "0")
        self.add_argument('--version',
                            help        = 'if specified, print version number',
                            type        = bool,
                            dest        = 'b_version',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
        self.add_argument("--jsonReturn",
                            help        = "output final return in json",
                            type        = bool,
                            dest        = 'jsonReturn',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """

        if options.b_version:
            print('Plugin Version: %s' % Freesurfer_pp.VERSION)
            sys.exit(0)

        if len(options.treePrint):
            str_tree = ''
            str_tree = Freesurfer_pp.dirTree_probe(options.treePrint, '')
            print(str_tree)
            sys.exit(0)

        if len(options.processDelay):
            print('Simulating a process delay of %s seconds...' % options.processDelay)
            time.sleep(int(options.processDelay))

        str_ageDirDefault   = '05-yr/02-mo/04-da'
        if len(options.ageSpec):
            l_ageSpec   = options.ageSpec.split('-')
            str_ageDir  = '%s-yr/%s-mo/%s-da' % (l_ageSpec[0], l_ageSpec[1], l_ageSpec[2])
        else:
            str_ageDir  = str_ageDirDefault

        str_treeSpec    = '../preprocessed/%s/stats' % str_ageDir
        if not os.path.isdir(str_treeSpec):
            print('It seems the ageSpec dir does not seem valid. Reverting to default.')
            str_treeSpec = '../preprocessed/%s/stats' % str_ageDirDefault            

        print('Deleting any existing data in output dir...')
        shutil.rmtree('%s/stats' % options.outputdir, ignore_errors = True)
        print('Copying tree from %s to output dir...' % str_treeSpec)
        shutil.copytree(str_treeSpec, '%s/stats' % options.outputdir)

# ENTRYPOINT
if __name__ == "__main__":
    app = Freesurfer_pp()
    app.launch()
