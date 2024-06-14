document.addEventListener("DOMContentLoaded", function () {
    new Vue({
        el: '#record-app',
        data: {
            userRecords: [],
            currentPage: 1,
            pageSize: 12,
        },
        computed: {
            paginatedRecords() {
                const start = (this.currentPage - 1) * this.pageSize;
                const end = start + this.pageSize;
                return this.userRecords.slice(start, end);
            }
        },
        mounted() {
            this.loadUserRecords();
        },
        methods: {
            handlePageChange(page) {
                this.currentPage = page;
            },
            loadUserRecords() {
                axios.get('/api/user_records/')
                    .then(response => {
                        this.userRecords = response.data;
                    })
                    .catch(error => {
                        console.error('Error loading user records:', error);
                        this.$message({
                            type: 'error',
                            message: '加载用户记录失败!'
                        });
                    });
            }
        }
    });
});
