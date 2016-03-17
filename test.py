import subprocess as sp
import shlex

question = 'What animals are those?'

command = "th predict.lua -checkpoint_file data/vqa_epoch23.26_0.4610_cpu.t7 -input_image_path test -question '" + question + "'"
args = shlex.split(command)
p = sp.check_output(args, cwd='/home/ubuntu/neural-vqa/')

print p