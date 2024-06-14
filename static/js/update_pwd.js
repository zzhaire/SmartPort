new Vue({
    el: '#update-pwd-app',
    data() {
        return {
            form: {
                current_pwd: '',
                new_pwd: '',
                confirm_pwd: ''
            }
        };
    },
    methods: {
        confirmSubmit() {
            this.$confirm('确定修改密码?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.submitForm();
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消修改密码'
                });
            });
        },
        submitForm() {
            // 提交表单逻辑
            console.log(this.form);
            // 发送POST请求到服务器
            fetch('/info/update_pwd/', {
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
                        type: data.success ? 'success' : 'error',
                        message: data.message
                    });
                    if (data.success) {
                        this.resetForm();
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        resetForm() {
            this.form.current_pwd = '';
            this.form.new_pwd = '';
            this.form.confirm_pwd = '';
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
