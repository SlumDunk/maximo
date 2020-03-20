import os
import time
import sys
import json
import numpy as np

from pathlib import Path

np.set_printoptions(threshold=np.inf)

input_path = os.path.curdir + "/maximos/input"
output_path = os.path.curdir + "/maximos/output"


def check_output_dir():
    output_dir = Path(output_path)
    if (not output_dir.exists()):
        output_dir.mkdir();


def convert2json(file, parent_path):
    temp = np.load(parent_path + '/' + file)

    Head = temp[0]
    Neck = temp[1]
    RightForeArm = temp[2]
    RightArm = temp[3]
    RightHand = temp[4]
    LeftArm = temp[5]
    LeftForeArm = temp[6]
    LeftHand = temp[7]
    Hips = temp[8]
    RightUpLeg = temp[9]
    RightLeg = temp[10]
    RightFoot = temp[11]
    LeftUpLeg = temp[12]
    LeftLeg = temp[13]
    LeftFoot = temp[14]
    frames = list()
    for sequence in range(1, int(np.shape(temp)[2])):
        np.around(LeftForeArm[0][sequence - 1], decimals=2)
        x = str(np.around(LeftForeArm[0][sequence - 1], decimals=2))
        y = str(np.around(LeftForeArm[1][sequence - 1], decimals=2))
        z = str(np.around(LeftForeArm[2][sequence - 1], decimals=2))
        leftForeArm = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(LeftArm[0][sequence - 1], decimals=2))
        y = str(np.around(LeftArm[1][sequence - 1], decimals=2))
        z = str(np.around(LeftArm[2][sequence - 1], decimals=2))
        leftShoulder = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(LeftHand[0][sequence - 1], decimals=2))
        y = str(np.around(LeftHand[1][sequence - 1], decimals=2))
        z = str(np.around(LeftHand[2][sequence - 1], decimals=2))
        leftHand = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(LeftFoot[0][sequence - 1], decimals=2))
        y = str(np.around(LeftFoot[1][sequence - 1], decimals=2))
        z = str(np.around(LeftFoot[2][sequence - 1], decimals=2))
        leftFoot = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(LeftLeg[0][sequence - 1], decimals=2))
        y = str(np.around(LeftLeg[1][sequence - 1], decimals=2))
        z = str(np.around(LeftLeg[2][sequence - 1], decimals=2))
        leftLeg = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(LeftUpLeg[0][sequence - 1], decimals=2))
        y = str(np.around(LeftUpLeg[1][sequence - 1], decimals=2))
        z = str(np.around(LeftUpLeg[2][sequence - 1], decimals=2))
        leftUpLeg = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(RightForeArm[0][sequence - 1], decimals=2))
        y = str(np.around(RightForeArm[1][sequence - 1], decimals=2))
        z = str(np.around(RightForeArm[2][sequence - 1], decimals=2))
        rightForeArm = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(RightArm[0][sequence - 1], decimals=2))
        y = str(np.around(RightArm[1][sequence - 1], decimals=2))
        z = str(np.around(RightArm[2][sequence - 1], decimals=2))
        rightShoulder = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(RightHand[0][sequence - 1], decimals=2))
        y = str(np.around(RightHand[1][sequence - 1], decimals=2))
        z = str(np.around(RightHand[2][sequence - 1], decimals=2))
        rightHand = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(RightFoot[0][sequence - 1], decimals=2))
        y = str(np.around(RightFoot[1][sequence - 1], decimals=2))
        z = str(np.around(RightFoot[2][sequence - 1], decimals=2))
        rightFoot = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(RightLeg[0][sequence - 1], decimals=2))
        y = str(np.around(RightLeg[1][sequence - 1], decimals=2))
        z = str(np.around(RightLeg[2][sequence - 1], decimals=2))
        rightLeg = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(RightUpLeg[0][sequence - 1], decimals=2))
        y = str(np.around(RightUpLeg[1][sequence - 1], decimals=2))
        z = str(np.around(RightUpLeg[2][sequence - 1], decimals=2))
        rightUpLeg = Location(",".join((x, y, z)), "0,0,0,0")

        x = str(np.around(Head[0][sequence - 1], decimals=2))
        y = str(np.around(Head[1][sequence - 1], decimals=2))
        z = str(np.around(Head[2][sequence - 1], decimals=2))
        head = Location(",".join((x, y, z)), "0,0,0,0")

        leftEye = Location("999,999,999,999", "0,0,0,0")
        rightEye = Location("999,999,999,999", "0,0,0,0")
        frame = Skeleton(leftForeArm, leftShoulder, leftHand, leftFoot, leftLeg, leftUpLeg, leftEye, rightForeArm,
                         rightShoulder,
                         rightHand, rightFoot, rightLeg, rightUpLeg, rightEye, head, sequence)
        frames.append(frame)
    out_dict = {"list": frames}
    return out_dict
    pass


def save(out_dict, file_path, file_name):
    parent = Path(file_path)
    if not parent.exists():
        os.makedirs(file_path)
    with open(os.path.join(file_path, file_name), 'w')as f:
        json.dump(out_dict, f, cls=ClsEncoder)
    pass


def search_files(parent_path):
    for root, dirs, files in os.walk(parent_path):
        if len(files) == 0:
            for dir in dirs:
                tmp_path = parent_path + "/" + dir
                search_files(tmp_path)
        else:
            for file in files:
                out_dict = convert2json(file, root)
                file_path = (root).replace('input', 'output')
                save(out_dict, file_path.replace('\\', '/'), file.replace('npy', 'json'))


class Skeleton:
    def __init__(self, LeftForeArm, LeftShoulder, LeftHand, LeftFoot, LeftLeg, LeftUpLeg, LeftEye, RightForeArm,
                 RightShoulder, RightHand, RightFoot, RightLeg, RightUpLeg, RightEye, Head, Sequence):
        self.LeftForeArm = LeftForeArm.to_str()
        self.LeftShoulder = LeftShoulder.to_str()
        self.LeftHand = LeftHand.to_str()
        self.LeftFoot = LeftFoot.to_str()
        self.LeftLeg = LeftLeg.to_str()
        self.LeftUpLeg = LeftUpLeg.to_str()
        self.LeftEye = LeftEye.to_str()
        self.RightForeArm = RightForeArm.to_str()
        self.RightShoulder = RightShoulder.to_str()
        self.RightHand = RightHand.to_str()
        self.RightFoot = RightFoot.to_str()
        self.RightLeg = RightLeg.to_str()
        self.RightUpLeg = RightUpLeg.to_str()
        self.RightEye = RightEye.to_str()
        self.Head = Head.to_str()
        self.Sequence = str(Sequence)

    pass


class Location:
    def __init__(self, position, rotation):
        self.position = position
        self.rotation = rotation

    def to_str(self):
        val = '{\"position\":\"(' +self.position+')\",\"rotation\":\"(' +self.rotation+')\"}'
        return val

    pass


def obj2dict(obj):
    memberlist = [m for m in dir(obj)]
    _dict = {}
    for m in memberlist:
        if m[0] != "_" and not callable(m):
            _dict[m] = getattr(obj, m)
    return _dict


class ClsEncoder(json.JSONEncoder):
    def default(self, o):
        return obj2dict(o)


if __name__ == '__main__':
    check_output_dir()
    search_files(input_path)
