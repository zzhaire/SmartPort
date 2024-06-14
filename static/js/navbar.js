document.addEventListener('DOMContentLoaded', function () {
    new Vue({
        el: '#navbar-app',
        data() {
            return {
                activeIndex: '1'
            };
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },
            navigateTo(url) {
                window.location.href = url;
            },
            logout() {
                // 发送 GET 请求以登出
                fetch("/logout", {
                    method: "GET"
                })
                    .then(function (response) {
                        if (response.ok) {
                            return response.json(); // 解析响应数据为 JSON
                        } else {
                            throw new Error("请求失败");
                        }
                    })
                    .then(function (responseData) {
                        // 在这里处理服务端返回的数据
                        console.log(responseData);
                        alert(responseData.message);

                        if (responseData.message === '登出成功') {
                            window.location.href = "/login";
                        }
                    })
                    .catch(function (error) {
                        // 请求失败的处理逻辑
                        console.error(error);
                    });
            }
        }
    });
});
