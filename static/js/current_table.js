new Vue({
    el: '#ocean-current-app',
    data() {
        return {
            oceanCurrentData: [],
            currentPage: 1,
            pageSize: 12
        };
    },
    computed: {
        paginatedData() {
            const start = (this.currentPage - 1) * this.pageSize;
            const end = this.currentPage * this.pageSize;
            // console.log(this.oceanCurrentData.slice(start, end))
            return this.oceanCurrentData.slice(start, end);
        }
    },
    methods: {
        getOceanCurrentData() {
            const oceanCurrentData = [];
            const rows = document.querySelectorAll('#ocean-current-data tr');
            rows.forEach(row => {
                const cols = row.children;
                oceanCurrentData.push({
                    time: cols[0].textContent,
                    silt_condition: cols[1].textContent,
                    depth: parseFloat(cols[2].textContent)
                });
            });
            this.initEcharts(oceanCurrentData);
            return oceanCurrentData;
        },
        handlePageChange(val) {
            this.currentPage = val;
        },
        initEcharts(data) {
            const depthChart = echarts.init(document.getElementById('echart-depth'));
            const siltChart = echarts.init(document.getElementById('echart-silt'));

            const times = data.map(item => item.time);
            const depths = data.map(item => item.depth);

            const siltConditions = data.map(item => item.silt_condition);
            const siltConditionCount = siltConditions.reduce((acc, condition) => {
                acc[condition] = (acc[condition] || 0) + 1;
                return acc;
            }, {});

            const siltData = Object.keys(siltConditionCount).map(key => ({
                name: key,
                value: siltConditionCount[key]
            }));

            depthChart.setOption({
                title: { text: '洋流深度变化' },
                xAxis: { type: 'category', data: times },
                yAxis: { type: 'value' },
                series: [{
                    data: depths,
                    type: 'line',
                    smooth: true,
                    lineStyle: { color: '#1E90FF' },
                    itemStyle: { color: '#1E90FF' }
                }]
            });

            siltChart.setOption({
                title: { text: '淤沙状态分布', left: 'center' },
                tooltip: { trigger: 'item' },
                series: [{
                    name: '淤沙状态',
                    type: 'pie',
                    radius: '50%',
                    data: siltData,
                    emphasis: {
                        itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)' }
                    }
                }]
            });
        }
    },
    mounted() {
        this.oceanCurrentData = this.getOceanCurrentData();
        this.initEcharts(this.oceanCurrentData);
    }
});
