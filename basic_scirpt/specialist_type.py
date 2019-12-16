"""自动化生成数据库中的专家分类表"""
#!/usr/bin/env python3
import re
import docx

import sys
import os
import django
sys.path.append('../')
os.environ['DJANGO_SETTINGS_MODULE'] = 'specialist_info.settings'
django.setup()

from Specialist.models import SpecialistCategory

def save(text):
    """将传入的字符串格式化后存入数据库
    分类ID: 如 A01 A0101
    分类名称:
    """
    ret = re.match(r'^\w{1}\d{2,6}', text)
    if ret:
        key = ret.group()
        val = re.split(r'^\w{1}\d{2,6} *', text)[1]
        val = val.replace('\n', '').replace('\r', '')
        obj = SpecialistCategory(key=key, name=val)
        obj.save()

def main():
    """main"""
    doc = docx.Document('type_info.docx')
    for table in doc.tables:
        for cell in table.columns[0].cells:
            save(cell.text)
        for cell in table.columns[1].cells:
            save(cell.text)

if __name__ == "__main__":
    main()
