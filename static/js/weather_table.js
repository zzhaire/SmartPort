new Vue({
    el: '#weather-app',
    data() {
        return {
            weatherData: [],
            currentPage: 1,
            pageSize: 12
        };
    },
    computed: {
        paginatedData() {
            const start = (this.currentPage - 1) * this.pageSize;
            const end = this.currentPage * this.pageSize;
            // console.log(this.weatherData.slice(start, end));
            return this.weatherData.slice(start, end);
        }
    },
    methods: {
        getWeatherData() {
            const weatherData = [];
            const rows = document.querySelectorAll('#weather-data tr');
            rows.forEach(row => {
                const cols = row.children;
                weatherData.push({
                    time: cols[0].textContent.trim(),
                    description: cols[1].textContent.trim(),
                    warning_level: cols[2].textContent.trim(),
                    temperature: parseFloat(cols[3].textContent),
                    rainfall: parseFloat(cols[4].textContent)
                });
            });
            this.initEcharts(weatherData);
            // console.log(weatherData)
            return weatherData;
        },
        getTagType(level) {
            switch (level) {
                case 'normal':
                    return 'success';
                case 'alert':
                    return 'warning';
                case 'danger':
                    return 'danger';
                default:
                    return '';
            }
        },
        getWarningText(level) {
            switch (level.trim()) {
                case 'normal':
                    return '正常';
                case 'alert':
                    return '警告';
                case 'danger':
                    return '危险';
                default:
                    return '';
            }
        },
        handlePageChange(val) {
            this.currentPage = val;
        },
        initEcharts(data) {
            const lineChart = echarts.init(document.getElementById('echart-line'));
            const pieChart = echarts.init(document.getElementById('echart-pie'));
            const tempChart = echarts.init(document.getElementById('echart-temp'));
            const rainfallChart = echarts.init(document.getElementById('echart-rainfall'));

            const times = data.map(item => item.time);
            const levels = data.map(item => {
                switch (item.warning_level.trim()) {
                    case 'normal':
                        return 1;
                    case 'alert':
                        return 2;
                    case 'danger':
                        return 3;
                }
            });

            const descriptions = data.map(item => item.description);
            const descriptionCount = descriptions.reduce((acc, desc) => {
                acc[desc] = (acc[desc] || 0) + 1;
                return acc;
            }, {});

            const pieData = Object.keys(descriptionCount).map(key => ({
                name: key,
                value: descriptionCount[key]
            }));

            const temperatures = data.map(item => item.temperature);
            const rainfalls = data.map(item => item.rainfall);

            lineChart.setOption({
                title: { text: '天气预警等级变化' },
                xAxis: { type: 'category', data: times },
                yAxis: { type: 'value', min: 1, max: 3 },
                series: [{
                    data: levels,
                    type: 'line',
                    smooth: true,
                    lineStyle: { color: '#5470C6' },
                    itemStyle: { color: '#5470C6' }
                }]
            });

            pieChart.setOption({
                title: { text: '天气描述占比', left: 'center' },
                tooltip: { trigger: 'item' },
                series: [{
                    name: '描述',
                    type: 'pie',
                    radius: '50%',
                    data: pieData,
                    emphasis: {
                        itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)' }
                    }
                }]
            });

            tempChart.setOption({
                title: { text: '气温变化' },
                xAxis: { type: 'category', data: times },
                yAxis: { type: 'value' },
                series: [{
                    data: temperatures,
                    type: 'line',
                    smooth: true,
                    lineStyle: { color: '#EE6666' },
                    itemStyle: { color: '#EE6666' }
                }]
            });

            rainfallChart.setOption({
                title: { text: '降雨量变化' },
                xAxis: { type: 'category', data: times },
                yAxis: { type: 'value' },
                series: [{
                    data: rainfalls,
                    type: 'line',
                    smooth: true,
                    lineStyle: { color: '#91CC75' },
                    itemStyle: { color: '#91CC75' }
                }]
            });

        }
    },
    mounted() {
        this.weatherData = this.getWeatherData();
        this.initEcharts(this.weatherData);
    }
});
