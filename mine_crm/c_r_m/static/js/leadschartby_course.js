var ctx = document.getElementById('courseChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels:["New Leads", "Followup Leads", "Prospects", "Registered", "Closed"],
                 datasets: [
              {
                label: "Python",
                borderColor:  'rgba(255, 99, 132, 0.2)',
                backgroundColor:  'rgba(255, 99, 132, 0.2)',
                pointRadius: 0,
                fill: false,
                borderWidth: 1,
                fill: 'origin',
                data: [55, 40, 15, 35, 25]
              },
              {
                label: "Java",
                borderColor: 'rgba(54, 162, 235, 0.2)',
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                pointRadius: 0,
                fill: false,
                borderWidth: 1,
                fill: 'origin',
                data: [40, 30, 20, 10, 50]
              },
              {
                label: "Web Designing",
                borderColor: 'rgba(255, 206, 86, 0.2)',
                backgroundColor: 'rgba(255, 206, 86, 0.2)',
                pointRadius: 0,
                fill: false,
                borderWidth: 1,
                fill: 'origin',
                data: [70, 10, 30, 40, 25]
              },
              {
                label: "Marketing",
                borderColor: 'rgba(75, 192, 192, 0.2)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                pointRadius: 0,
                fill: false,
                borderWidth: 1,
                fill: 'origin',
                data: [50, 10, 30, 40, 25]
              },

          ]
            },
            options: {
            maintainAspectRatio: false,
            responsive: false,
            width: 300,
            height: 100,
            }
        });

// Today Activities Chart

var activityData=[40,20,50,5,10,20,30]
var activitiesdata = {
  labels: ["Call","Message","Mail","Whatsapp","Counselling","College Visit","Corporate Visit"],
  datasets: [{
    label: 'Completed',
    data: activityData,
    backgroundColor: [
      'rgb(106, 90, 205,0.7)',
      'rgba(255, 99, 71, 0.7)',
      'rgb(60, 179, 113,0.7)',
      'rgba(75, 192, 192, 0.7)',
      'rgb(238, 130, 238,0.7)',
      'rgba(255, 159, 64, 0.7)',
      'rgb(255, 165, 0,0.7)'
    ],
    borderColor: [
      'rgb(106, 90, 205,1)',
      'rgba(255, 99, 71, 1)',
      'rgb(60, 179, 113,1)',
      'rgba(75, 192, 192, 1)',
      'rgb(238, 130, 238,1)',
      'rgba(255, 159, 64, 1)',
      'rgb(255, 165, 0,1)'
    ],
    borderWidth: 1,
    barPercentage:0.7,
    fill: false
  }]
};

// Get context with jQuery - using jQuery's .get() method.
if ($("#today_activities").length) {
  var barChartCanvas = $("#today_activities").get(0).getContext("2d");
  // This will get the first returned node in the jQuery collection.
  var activitiesChart = new Chart(barChartCanvas, {
    type: 'bar',
    data: activitiesdata,
    options: options
    });
  }