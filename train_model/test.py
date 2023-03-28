from os import listdir
from os.path import join, isfile
from demo import run_dehaze

test_root = 'Samples/'
model_path = 'model/'

def test(model_name):
    epoch_names = [f for f in listdir(model_path + model_name) if isfile(join(model_path + model_name, f))]
    test_cases = ['Thin_haze/','Moderate_haze/', 'Thick_haze/']
    
    for epoch_name in epoch_names:
        for test_case in test_cases:
            run_dehaze(test_root + test_case, epoch_name, model_name )