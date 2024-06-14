new Vue({
    el: '#user-info-app',
    data() {
        return {
            userInfo: {}
        };
    },
    methods: {
        fetchUserInfo() {
            axios.get(`/user_info/`)
                .then(response => {
                    this.userInfo = response.data;
                })
                .catch(error => {
                    console.error("There was an error!", error);
                });
        }
    },
    created() {
        this.fetchUserInfo();
    }
});
