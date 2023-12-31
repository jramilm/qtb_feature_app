var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}

function changeChevron(anchor) {
  var icon = anchor.querySelector("i");
  icon.classList.toggle('fa-chevron-down');
  icon.classList.toggle('fa-chevron-up');
}

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

function submitForm(event) {
    event.preventDefault();

    document.getElementById('search-form').submit();
}

const form = document.getElementById('search-form');
const submitIcon = document.getElementById('submit-icon');

submitIcon.addEventListener('mousedown', submitForm);

function toggleReplyField() {
    var replyField = document.getElementById("replyField");
    var replyText = document.getElementById("replyText");

    if (replyField.style.width === "458px") {
        alert("Form submitted: " + replyField.value);

        replyField.style.right = "10px";
        replyField.style.width = "0px";
        replyText.innerText = "Reply";
        hideReport();

        replyField.value = "";
    } else {
        replyField.style.right = "40px";
        replyField.style.width = "458px";
        replyText.innerText = "Submit";
    }
}

function displayReport(clickedRow) {
    var popupFrame = document.getElementById("popupFrame");
    var groupFrame = document.getElementById('groupFrame')
    var groupFrame2 = document.getElementById('groupFrame2')
    var reportId = clickedRow.getAttribute('data-report-id');

    $.ajax({
        url: 'get_report_details/',
        method: 'GET',
        data: { report_id: reportId },
        success: function (data) {
            document.querySelector('.details-header p:nth-child(1)').innerText = 'Sender: ' + data.sender;
            document.querySelector('.details-header p:nth-child(2)').innerText = 'Date: ' + data.date;
            document.querySelector('.mail-field p').innerText = data.content;
            document.getElementById('report_' + reportId).classList.remove('unread')
        },
        error: function (error) {
            console.error('Error fetching report details:', error);
        }
    });

    popupFrame.classList.remove('hidden');
    groupFrame.classList.add('inactive');
    groupFrame2.classList.add('inactive');
}

function hideReport() {
    var popupFrame = document.getElementById("popupFrame");
    var groupFrame = document.getElementById('groupFrame')
    var groupFrame2 = document.getElementById('groupFrame2')
    var replyField = document.getElementById("replyField");
    var replyText = document.getElementById("replyText");

    popupFrame.classList.add('hidden');
    groupFrame.classList.remove('inactive');
    groupFrame2.classList.remove('inactive');
    replyField.style.right = "10px";
    replyField.style.width = "0px";
    replyText.innerText = "Reply";
    replyField.value = "";
}