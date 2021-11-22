#!/usr/bin/env bash

## test own script
python own.py \
--dataroot datasets/shrec_16 \
--name shrec16 \
--ncf 64 128 256 256 \
--pool_res 600 450 300 180 \
--norm group \
--resblocks 1 \
--export_folder meshes \