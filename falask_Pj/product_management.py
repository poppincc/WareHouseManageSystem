import json
from datetime import timedelta
from flask import Flask, url_for, render_template, request, redirect, session, Blueprint, jsonify
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
        val = request.form
        # username = request.form.get('username','')
        # password = request.form.get('pass','')
        print(val)

        data=addProductForm.data
        productCode=data['productcode'] # 不要写成productCode=request.data["productcode"]
        productType=data['producttype']
        client=data['client']
        entryClerk=data['entryclerk']
        insert_into_productInfo(productCode,productType,client,1,1,1,1,1,entryClerk)
        products = show_allproducts()
        # return render_template('show_products.html',products=products)
        return jsonify({'ok': True})
    else:return render_template('add_product.html',form=addProductForm)

# xijiawei
# jQuery测试
@product_management.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == "POST":
        # val = request.form.get('username','')
        # print(val)
        data = request.get_data()
        print("data: %s" %(data))
        json_data = request.get_json()
        print("json_data: %s" %(json_data))
        return jsonify({'ok': True})
    else: return render_template('test.html')

@product_management.route('/test2', methods=['GET', 'POST'])
def test2():
    if request.method == "POST":
        val = request.form
        print(val)
        return jsonify({'ok': True})
    else: return render_template('test.html')

@product_management.route('/test_table', methods=['GET', 'POST'])
def tabledata():
    if request.method == "POST":
        val = request.form
        print(val)
        return render_template('test_table.html')
    else: return render_template('test_table.html')