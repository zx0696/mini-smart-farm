// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// line Chart Example
// 라인그래프 1
var ctx = document.getElementById("main_line");

var placeData = JSON.parse(document.getElementById('jsonData').textContent);
console.log(placeData) ;
fin = JSON.parse(placeData) ;
console.log(fin) ;
var main_lbl_final = fin.main_line_lbl
console.log(main_lbl_final)
var main_val_final = fin.main_line_val
console.log(main_val_final)

var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: main_lbl_final,
    datasets: [{
      label: "시간별 내부온도 관측치",
      lineTension: 0.3,
      backgroundColor: "rgba(218,241,223,0.4)",
      borderColor: "rgba(95,196,118,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(95,196,118,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(90,194,114,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: main_val_final,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 10
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
// 라인그래프 2
var ctx2 = document.getElementById("main_line2");

var placeData2 = JSON.parse(document.getElementById('jsonData').textContent);
console.log(placeData) ;
fin2 = JSON.parse(placeData) ;
console.log(fin2) ;
var main_lbl_final2 = fin2.main_line_lbl2
console.log(main_lbl_final)
var main_val_final2 = fin2.main_line_val2
console.log(main_val_final)

var myLineChart2 = new Chart(ctx2, {
  type: 'line',
  data: {
    labels: main_lbl_final2,
    datasets: [{
      label: "시간별 내부습도 관측치",
      lineTension: 0.3,
      backgroundColor: "rgba(218,241,223,0.4)",
      borderColor: "rgba(95,196,118,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(95,196,118,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(90,194,114,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: main_val_final2,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 10
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
// 라인그래프 3
var ctx3 = document.getElementById("main_line3");

var placeData3 = JSON.parse(document.getElementById('jsonData').textContent);
console.log(placeData3) ;
fin3 = JSON.parse(placeData3) ;
console.log(fin3) ;
var main_lbl_final3 = fin3.main_line_lbl3
console.log(main_lbl_final)
var main_val_final3 = fin3.main_line_val3
console.log(main_val_final)

var myLineChart3 = new Chart(ctx3, {
  type: 'line',
  data: {
    labels: main_lbl_final3,
    datasets: [{
      label: "시간별 분무량",
      lineTension: 0.3,
      backgroundColor: "rgba(218,241,223,0.4)",
      borderColor: "rgba(95,196,118,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(95,196,118,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(90,194,114,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: main_val_final3,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 1000,
          maxTicksLimit: 10
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
// 라인그래프 4
var ctx4 = document.getElementById("main_line4");

var placeData4 = JSON.parse(document.getElementById('jsonData').textContent);
console.log(placeData4) ;
fin4 = JSON.parse(placeData4) ;
console.log(fin4) ;
var main_lbl_final4 = fin4.main_line_lbl4
console.log(main_lbl_final4)
var main_val_final4 = fin4.main_line_val4
console.log(main_val_final4)

var myLineChart4 = new Chart(ctx4, {
  type: 'line',
  data: {
    labels: main_lbl_final4,
    datasets: [{
      label: "시간별 총광량",
      lineTension: 0.3,
      backgroundColor: "rgba(218,241,223,0.4)",
      borderColor: "rgba(95,196,118,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(95,196,118,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(90,194,114,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: main_val_final4,
    }], 
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 10000,
          maxTicksLimit: 10
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});



// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// // Pie Chart Example
// var ctx = document.getElementById("main_pie");

// var pie_lbl_final = fin.main_line_lbl
// console.log(main_lbl_final)
// var pie_val_final = fin.main_line_val
// console.log(main_val_final)

// var myPieChart = new Chart(ctx, {
//   type: 'pie',
//   data: {
//     labels: pie_lbl_final,
//     datasets: [{
//       data: pie_val_final,
//       backgroundColor: ['#037F8C', '#205459', '#F2E7C4', '#F28F38', '#F25757', '#03738C', '#04BFAD', '#D9CE36',
//       '#F2E8B6','#F26B6B' ,'#153259'],
//     }],
//   },
// });


