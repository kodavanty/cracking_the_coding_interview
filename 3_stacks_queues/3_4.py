#!/usr/bin/python

import sys

'''
'''
class Tower:
    def __init__ (self, tower_num):
        self.tower_num = tower_num
        self.disks = []

    def add_disk (self, disk_num):
        self.disks.append(disk_num)

    def remove_disk (self):
        return self.disks.pop()

    def move_disk (self, source, dest):
        disk = source.remove_disk()
        print "Moving DISK-%u from TOWER-%u to TOWER-%u" % (disk, source.tower_num, dest.tower_num)
        dest.add_disk(disk)

    def move_disks (self, num_disks, source, temp, dest):
        if num_disks == 1:
            self.move_disk(source, dest)
        else:
            self.move_disks(num_disks-1, source, dest, temp)
            self.move_disk(source, dest)
            self.move_disks(num_disks-1, temp, source, dest)

def hanoi (k):
    towers = [None]*3
    for i in range(3):
        towers[i] = Tower(i+1)

    for i in range(k, 0, -1):
        towers[0].add_disk(i)

    print towers[0].disks, towers[2].disks
    towers[0].move_disks(k, towers[0], towers[1], towers[2])
    print towers[0].disks, towers[2].disks

if __name__ == "__main__":
    hanoi(5)
