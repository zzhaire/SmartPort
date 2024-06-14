new Vue({
    el: '#server-app',
    data() {
        return {
            activeName: 'first',
            form: {
                ship_id: '',
                type: '',
                services: [],
                contact_info: '',
                appointment_time: '',
                price: null,
                description: "",
                product_type: "",
                num: 0,
            },
        };
    },

    methods: {
        calculateMaintenancePrice() {
            // 计算船舶检修价格
            let price = 0;
            if (this.form.type === '小型船') {
                price += 100;
            } else if (this.form.type === '小型货船') {
                price += 200;
            } else if (this.form.type === '中型货轮') {
                price += 300;
            } else if (this.form.type === '大型船舶') {
                price += 400;
            }

            this.form.services.forEach(service => {
                if (service === '常规检修') {
                    price += 50;
                } else if (service === '船体补漆') {
                    price += 100;
                } else if (service === '船体保养') {
                    price += 150;
                } else if (service === '故障修复检测') {
                    price += 200;
                }
            });

            this.form.price = price;
            this.form.description = `
            船舶编号:${this.form.ship_id},
            船舶类型: ${this.form.type},
            服务: ${this.form.services.join(', ')},`;
        },
        calculateFuelPrice() {
            this.form.price = this.form.product_type * this.form.num;
            this.form.description = `
            船舶编号:${this.form.ship_id},
            船舶类型: ${this.form.type},
            燃油类型: ${this.form.product_type},
            数量: ${this.form.num},
            `;
            this.form.services = ['燃油舱建', this.form.product_type, "(¥/ml)", this.form.num, "(ml)"]
            // this.form.service.push(this.form.product_type)
            // this.form.service.push(this.form.num)
        },
        calculateHotel() {
            let pp;
            switch (this.form.product_type) {
                case "单人间": pp = '120'; break;
                case "双人间": pp = '200'; break;
                case "套房": pp = '400'; break;
                case "商务房": pp = '1000'; break;
                default:pp=0;break;
            }
            this.form.price = pp * this.form.num;
            this.form.description= `
            港口住宿,
            房间类型: ${this.form.product_type},
            单价:${pp} ¥/晚
            数量: ${this.form.num},
            `;
            this.form.services = ['港口住宿', this.form.product_type, pp,"(¥/晚)", "*", this.form.num]
        },
        submitForm() {
            axios.post('/server/', this.form)
                .then(response => {
                    console.log(response.data);
                    this.$message({
                        type: 'success',
                        message: '提交成功!'
                    });
                })
                .catch(error => {
                    console.error(error);
                    this.$message({
                        type: 'error',
                        message: '提交失败, 请刷新重试!'
                    });
                });
        },
        cleanForm() {
            this.form.ship_id = '',
                this.form.type = '',
                this.form.services = [],
                this.form.contact_info = '',
                this.form.appointment_time = '',
                this.form.price = null,
                this.form.description = ""
        }
    }
});
