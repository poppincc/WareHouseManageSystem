from datetime import timedelta
from flask import Flask, url_for, render_template, request, redirect, session,Blueprint
from model import User
from db import *
import config
import os

from form import *

#product_managent = Flask(__name__)
product_management=Blueprint('product_management',__name__)

# xijiawei
# 成品管理
@product_management.route('/product_management', methods=['GET', 'POST'])
def show_products():
    products=show_allproducts()
    return render_template('show_products.html',products=products)

@product_management.route('/add_product', methods=['GET', 'POST'])
def add_product():
    addProductForm=AddProductForm()
    # print(addProductForm.validate_on_submit())
    if addProductForm.validate_on_submit():
        data=addProductForm.data
        productCode=data['productcode'] # 不要写成productCode=request.data["productcode"]
        productType=data['producttype']
        client=data['client']
        entryClerk=data['entryclerk']
        insert_into_productInfo(productCode,productType,client,1,1,1,1,1,entryClerk)
        products = show_allproducts()
        return render_template('show_products.html',products=products)
    else:return render_template('add_product.html',form=addProductForm)