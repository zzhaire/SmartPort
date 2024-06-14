var user_data = user_data
console.log(user_data)
new Vue({
    el: '#info-app',
    data() {
        return {
            form: {
                user_id: '',
                ship_id: '', // 预填的船舶编号
                draft_depth: '', // 预填的吃水深度
                type: '', // 预填的船舶类型
                contact_info: '' // 预填的联系方式
            }
        };
    },
    mounted() {
        // 从隐藏的表格中读取数据
        const userDataElement = document.getElementById('user-data');
        this.form.user_id = userDataElement.getAttribute('data-user_id');
        this.form.ship_id = userDataElement.getAttribute('data-ship_id');
        this.form.draft_depth = userDataElement.getAttribute('data-draft_depth');
        this.form.type = userDataElement.getAttribute('data-type');
        this.form.contact_info = userDataElement.getAttribute('data-contact_info');
    },
    methods: {
        confirmSubmit() {
            this.$confirm('确定提交更改?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.submitForm();
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消提交'
                });
            });
        },
        submitForm() {
            // 提交表单逻辑
            console.log(this.form);
            // 发送POST请求到服务器
            fetch('/info/change/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify(this.form)
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    this.$message({
                        type: 'success',
                        message: data.message
                    });
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        confirmUpdatePwd() {
            this.$confirm('确定修改密码?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                window.location.href = "/info/update_pwd"; // 跳转到修改密码页面
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消修改密码'
                });
            });
        },
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    }
});
