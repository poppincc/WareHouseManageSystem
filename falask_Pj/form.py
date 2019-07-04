from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField,DateField
from wtforms.validators import DataRequired,Length #引入Form验证父类


class LoginForm(Form):
    # 用户名
    account = StringField(
        # 标签
        label="账号",
        # 验证器
        validators=[
            DataRequired('请输入用户名')
        ],
        description="账号",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号!",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )

    # 密码
    pwd = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码')
        ],
        description="密码",

        # 附加选项(主要是前端样式),会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'
            # 表示输入框不能为空
        }
    )

    # 提交
    submit = SubmitField(
        label="添加",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

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


