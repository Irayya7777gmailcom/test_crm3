var ctx = document.getElementById('today_activities').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels:["Naukri", "Indeed", "Mail", "Whatsapp", "Foundit","Just Dial"],
                datasets: [{ 
                    label:'Source',
                    data:[100, 20, 30, 40, 50,25],
                    backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
                    borderWidth: 0.5
                }]
            },
            options: {
            maintainAspectRatio: false,
            responsive: false,
            width: 100,
            height: 100,
            }
        });