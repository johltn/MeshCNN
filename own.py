from options.test_options import TestOptions
from data import DataLoader
from models import create_model
from util.writer import Writer

opt = TestOptions().parse()
opt.serial_batches = True  # no shuffle
dataset = DataLoader(opt)
model = create_model(opt)

import pdb; pdb.set_trace()

# writer = Writer(opt)
# # test
# writer.reset_counter()
# for i, data in enumerate(dataset):
#     model.set_input(data)
#     ncorrect, nexamples = model.test()
#     writer.update_counter(ncorrect, nexamples)
# writer.print_acc(epoch, writer.acc)



