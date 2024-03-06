#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:58:04 2024

@author: chenbailun
"""

def main():
    num = int(input("請輸入一個整數："))

    if num % 2 == 0:
        print(num, "是偶數。")
    else:
        print(num, "不是偶數。")

if __name__ == "__main__":
    main()
