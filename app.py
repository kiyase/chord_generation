import gradio as gr
import shutil
import os
from config import *

file_folder=OUTPUTS_PATH

def clear_folder(folder_path):
    # 获取文件夹中的所有文件列表
    file_list = os.listdir(folder_path)

    # 逐个删除文件
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


def chord_generate(upload):
    # 指定要保存的文件夹路径
    save_folder =INPUTS_PATH  # 将此行替换为您要保存的文件夹路径

    # 保存上传的MIDI文件到指定文件夹中
    save_path = os.path.join(save_folder)
    shutil.copy(upload.name, save_path)
    #旋律续写
    os.system("python harmonizer.py")
    file_name = os.path.splitext(os.path.basename(upload.name))[0]
    file_path=os.path.join(str(file_folder)+"/"+str(file_name)+".mxl")
    #clear_folder("chord_generation/inputs")
    return file_path
    
in_file=gr.File(label="请上传您的midi音频文件",file_types=["MIDI"])
out_file=gr.File(label="输出带和弦伴奏的XML文件")
melody_iface=gr.Interface(fn=chord_generate,inputs=in_file,outputs=out_file,title="和弦自动生成")
melody_iface.launch()

