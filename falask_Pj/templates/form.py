from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import Required

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