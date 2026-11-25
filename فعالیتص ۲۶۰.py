# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:41:34 2026

@author: Sam-Tech
"""

from pathlib import Path

file_path = Path('mobile_brands.txt')
brands = file_path.read_text()
brands = file_path.read_text().rstrip()
brands = brands.splitlines()

brand_text = ""

for brand in brands:
    brand_text += brand.rstrip() + " - " 
    print(brand_text)