
// ======================== Editing Profile ===========================

var is_editing = false;
function EditProfile() {
  edit_button = document.getElementById("edit-button");
  view = document.getElementById("edit-form-view");
  edit = document.getElementById("edit-form-edit");
  if (is_editing) {
    is_editing = false;
    edit.style.display = "none";
    view.style.display = "inline-block";
  } else {
    is_editing = true;
    view.style.display = "none";
    edit.style.display = "inline-block";
  }
  $("#edit-form-edit a").html("link")
}

function ShowDetail(element) {
  var id = element.id;
  var form = document.getElementById(id+"-form");
  if (form.style.display != "inline-block") {
    form.style.display = "inline-block";
  } else {
    form.style.display = "none";
  }
};

function ShowSibling(element) {
  var id = element.id;
  var form = document.getElementById(id+"-siblings");
  if (form.style.display != "inline-block") {
    form.style.display = "inline-block";
    element.innerHTML = "Hide All Recurrings"
  } else {
    form.style.display = "none";
    element.innerHTML = "Show All Recurrings"
  }
};

function toggleChatOrg() {
  const currUser = JSON.parse(document.getElementById('currUser').textContent)
      .replace(/[^\w\s\']|_/g, "")
      .replace(/\s+/g, " ");
  const profileUser = JSON.parse(document.getElementById('profileUser').textContent)
      .replace(/[^\w\s\']|_/g, "")
      .replace(/\s+/g, " ");
  window.location.pathname = "chatroom/" + profileUser+"_"+currUser+ "/";
}
function toggleChatVol() {
  const currUser = JSON.parse(document.getElementById('currUser').textContent)
      .replace(/[^\w\s\']|_/g, "")
      .replace(/\s+/g, " ");
  const profileUser = JSON.parse(document.getElementById('profileUser').textContent)
      .replace(/[^\w\s\']|_/g, "")
      .replace(/\s+/g, " ");
  window.location.pathname = "chatroom/" + currUser+"_"+profileUser+ "/";
}