// ==========================
// Create Map
// ==========================
const map = L.map("map").setView([12.9716, 77.5946], 12);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

// ==========================
// Icons
// ==========================
const ambulanceIcon = L.divIcon({
    html: '<i class="fa-solid fa-truck-medical" style="color:red;font-size:24px;"></i>',
    className: "",
    iconSize: [30, 30]
});

const hospitalIcon = L.divIcon({
    html: '<i class="fa-solid fa-hospital" style="color:#2563eb;font-size:24px;"></i>',
    className: "",
    iconSize: [30, 30]
});

const disasterIcon = L.divIcon({
    html: '<i class="fa-solid fa-fire" style="color:orange;font-size:28px;"></i>',
    className: "",
    iconSize: [30, 30]
});

const hqIcon = L.divIcon({
    html: '<i class="fa-solid fa-shield-heart" style="color:lime;font-size:26px;"></i>',
    className: "",
    iconSize: [30, 30]
});

// ==========================
// HQ
// ==========================
L.marker([12.9716, 77.5946], {
    icon: hqIcon
})
.addTo(map)
.bindPopup("🚨 Disaster Response HQ");

// ==========================
// Dashboard Elements
// ==========================
const disasterCount = document.getElementById("totalIncidents");
const disasterType = document.getElementById("disasterType");

const selectedDisaster = document.getElementById("selectedDisaster");
const ambulanceRequired = document.getElementById("ambulanceRequired");
const teamRequired = document.getElementById("teamRequired");

const nearestAmbulance = document.getElementById("nearestAmbulance");
const nearestHospital = document.getElementById("nearestHospital");

const distanceText = document.getElementById("distance");
const etaText = document.getElementById("eta");
const statusText=document.getElementById("status");

const severityText=document.getElementById("severity");

const confidenceText=document.getElementById("confidence");

const reasonList=document.getElementById("reasonList");

let totalDisasters = 0;

let disasterMarker = null;
let ambulanceRoute = null;
let hospitalRoute = null;

// ==========================
// Ambulances
// ==========================
const ambulances = [

{
id:"A1",
lat:12.9716,
lng:77.5946,
available:true
},

{
id:"A2",
lat:12.9810,
lng:77.6050,
available:false
},

{
id:"A3",
lat:12.9615,
lng:77.5800,
available:true
},

{
id:"A4",
lat:12.9500,
lng:77.6100,
available:true
}

];

ambulances.forEach(a=>{

L.marker([a.lat,a.lng],{
icon:ambulanceIcon
})
.addTo(map)
.bindPopup(
`🚑 ${a.id}<br>
Status : ${a.available ? "Available ✅" : "Busy ❌"}`
);

});

// ==========================
// Hospitals
// ==========================
const hospitals = [

{
id:"H1",
lat:12.9645,
lng:77.5930,
capacity:50,
occupied:20
},

{
id:"H2",
lat:12.9850,
lng:77.6200,
capacity:30,
occupied:30
},

{
id:"H3",
lat:12.9505,
lng:77.5820,
capacity:40,
occupied:12
},

{
id:"H4",
lat:12.9755,
lng:77.5700,
capacity:25,
occupied:25
}

];

hospitals.forEach(h=>{

L.marker([h.lat,h.lng],{
icon:hospitalIcon
})
.addTo(map)
.bindPopup(
`🏥 ${h.id}<br>
Beds : ${h.capacity-h.occupied}/${h.capacity}`
);

});
// ==========================
// Click Event
// ==========================
map.on("click", function (e) {

    const lat = e.latlng.lat;
    const lng = e.latlng.lng;

    totalDisasters++;
    disasterCount.innerText = totalDisasters;

    // Remove previous disaster marker
    if (disasterMarker) {
        map.removeLayer(disasterMarker);
    }

    // Remove previous routes
    if (ambulanceRoute) {
        map.removeLayer(ambulanceRoute);
    }

    if (hospitalRoute) {
        map.removeLayer(hospitalRoute);
    }

    // Add new disaster marker
    disasterMarker = L.marker([lat, lng], {
        icon: disasterIcon
    })
    .addTo(map)
    .bindPopup("🔥 Disaster Reported")
    .openPopup();

    // ==========================
    // Call Flask AI
    // ==========================
    fetch("/api/dispatch", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            lat: lat,
            lng: lng,
            disaster: disasterType.value

        })

    })

    .then(response => response.json())

    .then(result => {

        // ==========================
        // Dashboard
        // ==========================

        selectedDisaster.innerText = disasterType.value;

severityText.innerText = result.severity;

confidenceText.innerText =
result.confidence + "%";

ambulanceRequired.innerText =
result.resources.ambulances;

teamRequired.innerText =
result.resources.teams;

nearestAmbulance.innerText =
result.ambulance.id;

nearestHospital.innerText =
result.hospital.id;

distanceText.innerText =
result.distance + " km";

etaText.innerText =
result.eta + " min";

statusText.innerText =
"🚑 AI Resources Allocated";
// ==========================
// AI Reasoning
// ==========================

reasonList.innerHTML = "";

result.reason.forEach(reason => {

    const item = document.createElement("li");

    item.innerText = reason;

    reasonList.appendChild(item);

});

        // ==========================
        // Find Ambulance
        // ==========================

        const ambulance = ambulances.find(a =>
            a.id === result.ambulance.id
        );

        // ==========================
        // Find Hospital
        // ==========================

        const hospital = hospitals.find(h =>
            h.id === result.hospital.id
        );

        // ==========================
        // Draw Ambulance Route
        // ==========================

        ambulanceRoute = L.polyline(

            [
                [ambulance.lat, ambulance.lng],
                [lat, lng]
            ],

            {
                color: "lime",
                weight: 6
            }

        ).addTo(map);

        // ==========================
        // Draw Hospital Route
        // ==========================

        hospitalRoute = L.polyline(

            [
                [lat, lng],
                [hospital.lat, hospital.lng]
            ],

            {
                color: "red",
                weight: 5,
                dashArray: "10,10"
            }

        ).addTo(map);

        console.log("AI Decision");
        console.log(result);
        loadHistory();
loadStatistics();

    })

    .catch(error => {

        console.error(error);

        alert("❌ Unable to connect to Flask Backend");

    });

});
// =====================================
// Load Incident History
// =====================================

function loadHistory() {

    fetch("/api/history")
        .then(response => {

            if (!response.ok) {
                throw new Error("Server Error");
            }

            return response.json();

        })
        .then(data => {

            const tableBody =
                document.querySelector("#historyTable tbody");

            tableBody.innerHTML = "";

            data.forEach(item => {

                const row = `
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.disaster}</td>
                        <td>${item.ambulance}</td>
                        <td>${item.hospital}</td>
                        <td>${item.eta} min</td>
                    </tr>
                `;

                tableBody.innerHTML += row;

            });

        })
        .catch(error => {

            console.error("History Error:", error);

        });

}

// =====================================
// Dashboard Statistics
// =====================================

function loadStatistics() {

    fetch("/api/statistics")
        .then(response => {

            if (!response.ok) {
                throw new Error("Server Error");
            }

            return response.json();

        })
        .then(data => {

            document.getElementById("totalIncidents").innerText =
                data.total_incidents;

            document.getElementById("fireCount").innerText =
                data.disaster_statistics.Fire || 0;

            document.getElementById("floodCount").innerText =
                data.disaster_statistics.Flood || 0;

            document.getElementById("earthquakeCount").innerText =
                data.disaster_statistics.Earthquake || 0;

        })
        .catch(error => {

            console.error("Statistics Error:", error);

        });

}

// =====================================
// Initial Load
// =====================================

loadHistory();
loadStatistics();

// =====================================
// Auto Refresh
// =====================================

setInterval(loadHistory, 5000);
setInterval(loadStatistics, 5000);