# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# less required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Config for train and eval."""
cfg_res50 = {
    'name': 'Resnet50',
    'min_sizes': [[16, 32], [64, 128], [256, 512]],
    'steps': [8, 16, 32],
    'variance': [0.1, 0.2],
    'clip': False,
    'loc_weight': 2.0,
    'class_weight': 1.0,
    'landm_weight': 1.0,
    'batch_size': 8,
    'num_workers': 8,
    'num_anchor': 29126,
    'ngpu': 3,
    'epoch': 100,
    'decay1': 70,
    'decay2': 90,
    'image_size': 840,
    'return_layers': {'layer2': 1, 'layer3': 2, 'layer4': 3},
    'in_channel': 256,
    'out_channel': 256,
    'match_thresh': 0.35,
    'optim': 'sgd',
    'warmup_epoch': -1,
    'initial_lr': 0.001,
    'network': 'resnet50',

    # opt
    'momentum': 0.9,
    'weight_decay': 5e-4,

    # lr
    'gamma': 0.1,

    # checkpoint
    'ckpt_path': './checkpoint/',
    'save_checkpoint_steps': 1000,
    'keep_checkpoint_max': 1,
    'resume_net': None,

    # dataset
    'training_dataset': './data/widerface/train/label.txt',
    'pretrain': True,
    'pretrain_path': './data/res50_pretrain.ckpt',

    # val
    'val_model': './checkpoint/ckpt_0/RetinaFace-100_536.ckpt',
    'val_dataset_folder': './data/widerface/val/',
    'val_origin_size': False,
    'val_confidence_threshold': 0.02,
    'val_nms_threshold': 0.4,
    'val_iou_threshold': 0.5,
    'val_save_result': False,
    'val_predict_save_folder': './widerface_result',
    'val_gt_dir': './data/ground_truth/',

}
