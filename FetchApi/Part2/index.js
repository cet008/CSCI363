function getNewMount() {
	random = Math.ceil(Math.random() * 200)
	var url = "https://ffxivcollect.com/api/mounts/" + random

	console.log("making fetch to", url)
	
	fetch(url)
		.then(resp=>{return resp.json()})
		.then(json=>{
			console.log(json)

			document.getElementById("mountImage").src = json.image
			document.getElementById("Name").textContent = json.name
			document.getElementById("Desc").textContent = json.description
		})

}


document.addEventListener("DOMContentLoaded", () => {
  console.log("Hello World!");
});