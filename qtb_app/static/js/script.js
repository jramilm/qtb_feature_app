document.addEventListener('DOMContentLoaded', function() {
    var data = {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [{
                label: '2021',
                data: [85, 88, 90, 92, 95, 93, 56, 98, 65, 83, 94, 96],
                borderColor: 'rgba(255, 99, 132, 1)',
                backgroundColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 2,
                fill: false,
            },
            {
                label: '2022',
                data: [76, 92, 45, 88, 34, 93, 76, 43, 99, 95, 96, 97],
                borderColor: 'rgba(54, 162, 235, 1)',
                backgroundColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                fill: false,
            },
            {
                label: '2023',
                data: [92, 94, 96, 98, 53, 95, 64, 91, 93, 86, 96, 98],
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false,
            },
        ]
    };

    var options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                type: 'category',
                labels: data.labels,
            },
            y: {
                beginAtZero: true,
                max: 100,
            }
        }
    };

    var ctx = document.getElementById('performanceChart').getContext('2d');

    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: options,
    });
});