# Install hints
Before using script, you must make initial system setup on your own. 
Script only installs and configures software 

## Internet connection
### WIFI:
```bash
iwctl
[iwd] station interface_name scan # usually interface_name == wlan0
[iwd] station interface_name get-networks
[iwd] station interface_name connect network_name
```
### Wired
- Should be working out of the box. If not - something is wrong

Verify connection with `ping google.com`

## Pacman-keys
```bash
pacman-key --init
pacman-key --populate archlinux
```

## archinstall
Last time I tried, archinstall didn't work in my system with dualboot, and didnt' work in virtual box VM.
If anything changes, I recomend using it, but for now I will do everything manually

## Base setup

### Time synchronization
```bash
timedatectl set-ntp true
```
### Disk partitioning
Make sure you're having GPT paritioning. If not, change to GPT by
```bash
sgdisk -g /dev/...
```

```bash
fdisk /dev/dev/nvme0n1
```
cheatsheet: 
- `m` - help 
- `p` - print current partitioning
- `n` - new parition
- `d` - delete parition
- `t` - change partition name
- `q` - exit without changes
- `w` - exit with changes written

#### Create filesystem on new paritions and mount them
```bash
# 1. Root
mkfs.ext4 /dev/nvme0n1p{root number} -L "ARCH"
mount /dev/nvme0n1p{root number} /mnt

# 2. Boot
mkdir -p /mnt/boot
mkfs.fat -F32 /dev/nvme0n1p{boot number}
mount /dev/nvme0n1p{boot number} /mnt/boot
```

## Archlinux install & setup
```bash
pacman  -Syy                                # Update pacman
pacstrap -K /mnt base linux linux-firmware  # Essential packages

genfstab -U /mnt >> /mnt/etc/fstab          # fstab

arch-chroot /mnt                            # change root
pacman -S vim sudo

# Time zone
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
hwclock --systohc

# Locales
vim /etc/locale.gen
# Uncomment en_US.UTF-8 UTF-8 and uk_UA.UTF-8 UTF-8
locale-gen

# Network configuration
echo 'archlinux-pasha' >> /etc/hostname    # Replace 'archlinux-pasha' with your hostname

# User configuration
passwd                                      # Change root password
useradd -G wheel -s /bin/bash -m pasha   # Replace 'pasha' with your username
visudo  # uncomment %wheel ALL=(ALL) ALL
passwd pasha

# Some other packages
pacman -S netctl htop git networkmanager
```

## Bootloader
```bash
bootctl install

vim /boot/loader/loader.conf
#       default arch
#       timeout 0
#       editor 0

pacman -S amd-ucode     # or interl-ucode
pacman -S linux

vim /boot/loader/entries/arch.conf
#       title Arch Linux
#       linux /vmlinuz-linux
#       initrd /intel-ucode.img
#       initrd /initramfs-linux.img
#       options root="LABEL=ARCH" rw
```

## Exit and reboot into installed system
```bash
exit
umount -R /mnt
reboot
```