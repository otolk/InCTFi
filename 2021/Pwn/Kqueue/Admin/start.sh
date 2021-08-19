#!/bin/bash

#stty intr ^]
stty sane
exec qemu-system-x86_64 \
    -cpu kvm64 \
    -m 512 \
    -nographic \
    -kernel "bzImage" \
    -append "console=ttyS0 oops=panic panic=-1 pti=off kaslr quiet" \
    -monitor /dev/null \
    -initrd "./rootfs.cpio" \
    -s
