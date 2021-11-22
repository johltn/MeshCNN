from options.test_options import TestOptions
from data import DataLoader
from models import create_model
from util.writer import Writer

opt = TestOptions().parse()
opt.serial_batches = True  # no shuffle
dataset = DataLoader(opt)
model = create_model(opt)


# Some quick snippet 
L = list(dataset)
model.set_input(L[0])
res = model.net(model.edge_features, model.mesh)
accuracy = model.get_accuracy(res.data.max(1)[1], model.labels)

import pdb; pdb.set_trace()

# writer = Writer(opt)
# # test
# writer.reset_counter()
# for i, data in enumerate(dataset):
#     model.set_input(data)
#     ncorrect, nexamples = model.test()
#     writer.update_counter(ncorrect, nexamples)
# writer.print_acc(epoch, writer.acc)



