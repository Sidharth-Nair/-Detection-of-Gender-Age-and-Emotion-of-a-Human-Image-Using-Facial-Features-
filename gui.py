# Employee churn prediction GUI
from tkinter import *
from tkinter import messagebox
from openpyxl import load_workbook
import xlrd
import pandas as pd
from auto_tqdm import tqdm
from PIL import Image, ImageTk
import tkinter as tk
import cv2


def adds(add,image):
    dim = (1080, 750)
    path="Images/"+image
    frame=cv2.imread(path)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("frame",resized)


