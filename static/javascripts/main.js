const colors = ['dark', 'yellow', 'green', 'blue', 'red', 'undefined', 'undefined', 'undefined', 'undefined'];

function checkState(checkbox) {
    const sidebarElement = document.getElementById("sidebar_item");
    const colorName = checkbox.value;
    const name = checkbox.name;
    if (checkbox.checked) {
        const clonedElement = sidebarElement.cloneNode(true);
        clonedElement.setAttribute("id", "sidebar_item_" + colorName + "_" + name);
        const color = colorPicker(colorName);
        clonedElement.classList.add("bg-" + colorName, "remove", "sidebar-item-flag");
        clonedElement.firstElementChild.lastElementChild.lastElementChild.innerText = name;
        const picturePath = checkbox.parentNode.parentNode.parentNode.firstElementChild.classList[1];
        clonedElement.firstElementChild.lastElementChild.firstElementChild.className = "fi " + picturePath + " sidebar-icon";
        const input = clonedElement.firstElementChild.firstElementChild;
        input.value = colorName;
        input.name = name;
        document.getElementById("sidebar-content").appendChild(clonedElement);
        setTimeout(function() {
            clonedElement.classList.remove("remove");
        }, 0);
    } else {
        const elementToRemove = document.getElementById("sidebar_item_" + colorName + "_" + name);
        deleteSidebarElement(elementToRemove);
    }
}
function deleteSidebarElement(item) {
    const idSplitted = item.id.split("_");
    item.classList.add("remove");
    const checkbox = document.getElementById(idSplitted[2] + "_" + idSplitted[3]);
    if (checkbox)
        checkbox.checked = false;
    setTimeout(function() {
        item.parentNode.removeChild(item);
    }, 200);
}

// function createSidebarElement(id, path) {
//     const sidebarText = document.createElement("p");
//     sidebarText.innerText = id.split("-")[-1];
//
//     const sidebarIcon = document.createElement("i");
//     sidebarIcon.className = path + " sidebar-icon"
//
//     const sidebarItemContent = document.createElement("div");
//     sidebarItemContent.className = "sidebar-item-content";
//     sidebarItemContent.appendChild(sidebarIcon)
//     sidebarItemContent.appendChild(sidebarText)
//
//
//
//     const sidebarElement = document.createElement("div");
//     sidebarElement.id = "sidebar-item-" + id;
// }

function createBubble(count) {
    for(let i = 0; i < count; i++) {
        const bubble = document.createElement("div");
        const color = colors[colors.length%(i+1)];
        bubble.classList.add("bubble");
        bubble.style.position = "fixed";
        const size = Math.random() * 240 + 24 + "px";
        bubble.style.width = size;
        bubble.style.height = size;
        bubble.style.left = Math.random() * 100 + "%";
        bubble.style.top = Math.random() * 100 + "%";
        bubble.style.background = colorPicker(color);
        bubble.style.zIndex = -1;
        bubble.style.opacity = 0.3;
        bubble.style.borderRadius = "50%";
        document.getElementsByTagName("body")[0].appendChild(bubble);
    }
}

// function to create 3 diagonal colored areas as background
function createDiagonalAreas() {
    const colors = ['dark', 'yellow', 'green', 'blue', 'red'];
    const body = document.getElementsByTagName("body")[0];
    for(let i = 0; i < 3; i++) {
        const area = document.createElement("div");
        area.classList.add("area");
        area.classList.add("bg-" + colors[i]);
        area.style.zIndex = -1;
        area.style.opacity = 0.5;
        area.style.position = "fixed";
        area.style.width = "100%";
        area.style.height = "100%";
        area.style.transform = "rotate(" + (i * 45) + "deg)";
        body.appendChild(area);
    }
}

function clearBasket(formid) {
    const form = document.getElementById(formid);
    const basket = document.getElementsByClassName("sidebar-item-flag");
    for(let i = 0; i < basket.length; i++) {
        deleteSidebarElement(basket[i]);
    }
    setTimeout(function() {
        if(form) {
            form.submit();
        }
    }, 400);
}

function colorPicker(name) {
    switch (name) {
        case "white":
            return "#fcfcfc";
        case "dark":
            return "#5C5E6B";
        case "blue":
            return "#378495";
        case "green":
            return "#68A357";
        case "yellow":
            return "#FFA90A";
        case "red":
            return "#B73315";
        default:
            return "#ECEDEE";
    }
}