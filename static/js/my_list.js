new Vue({
    el: '#record-table-app',
    data() {
        return {
            records: [],
            pagedRecords: [],
            currentPage: 1
        };
    },
    methods: {
        fetchRecords() {
            axios.get(`/get_list/`)
                .then(response => {
                    this.records = JSON.parse(response.data);
                    console.log(this.records)
                    this.$message({
                        type: 'success',
                        message: '查询订单成功'
                    });
                })
                .catch(error => {
                    console.error("There was an error!", error);
                });
        },
        viewDetails(record) {
            this.$alert(`消费详情: ${record.fields.server_details}`, '消费详情', {
                confirmButtonText: '确定'
            });
        },
        handlePageChange(page) {
            this.currentPage = page;
            this.setPageRecords();
        },
        setPageRecords() {
            const start = (this.currentPage - 1) * 12;
            const end = start + 12;
            this.pagedRecords = this.records.slice(start, end);
        }
    },
    created() {
        this.fetchRecords();
    }
});
