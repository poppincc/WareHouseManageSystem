from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import Required
from wtforms.validators import DataRequired # 引入Form验证父类

# 添加人员表单
from db import cc_findname


class MyForm(Form):
    status = SelectField('物料权限', validators=[Required()], choices=[('0', '无权限'), ('1', '查看（无金额）'), ('2', '查看（有金额）'), ('3', '修改')])
    statusPro = SelectField('成品权限', validators=[Required()], choices=[('0', '无权限'), ('1', '查看（无金额）'), ('2', '查看（有金额）'), ('3', '修改')])
    statusPur = SelectField('采购权限', validators=[Required()], choices=[('0', '无权限'), ('1', '查看（无金额）'), ('2', '查看（有金额）'), ('3', '修改')])

# 删除人员表单
class SelectForm(Form):
    result = cc_findname()
    personName = SelectField('用户姓名', validators=[Required()], choices=result)

# xijiawei
# 添加成品表单
class AddProductForm(Form):
    # 成品编号
    productcode = StringField(
        # 标签
        label="成品编号",
        # 验证器
        validators=[
            DataRequired('请输入成品编号')
        ],
        description="成品编号",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入成品编号",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )
    # 成品编号
    producttype = StringField(
        # 标签
        label="成品类型",
        # 验证器
        validators=[
            DataRequired('请输入成品类型')
        ],
        description="成品类型",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入成品类型",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )
    # 成品编号
    client = StringField(
        # 标签
        label="客户",
        # 验证器
        validators=[
            DataRequired('请输入客户名称')
        ],
        description="客户名称",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入客户名称",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )
    # 成品编号
    entryclerk = StringField(
        # 标签
        label="录入员",
        # 验证器
        validators=[
            DataRequired('请输入录入员姓名')
        ],
        description="录入员",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入录入员姓名",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )

    # 提交
    submit = SubmitField(
        label="添加",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )
