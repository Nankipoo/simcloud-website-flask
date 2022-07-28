//NAVIGATION BAR

var defaultColour = $(".nav-link").css("color", "whitesmoke");

var hoverColour = $(".nav-link").hover(
  function () {
    $(this).css("color", "white");
  },
  function () {
    $(this).css("color", "whitesmoke");
  }
);

var clickedColour = $(".nav-link").click(function () {
  $(this).css("color", "gold");
});

//SMALL IMAGES

var defaultColour2 = $(".click-here").css("color", "whitesmoke");

var hoverColour2 = $(".click-here").hover(
  function () {
    $(this).css("color", "white");
  },
  function () {
    $(this).css("color", "whitesmoke");
  }
);

var clickedColour2 = $(".click-here").click(function () {
  $(this).css("color", "gold");
});

const boxes = document.querySelectorAll(".box");

window.addEventListener("scroll", check_animation);

check_animation();

function check_animation() {
  const trigger = (window.innerHeight / 6) * 4;

  boxes.forEach((box) => {
    console.log(box);
    const top = box.getBoundingClientRect().top;

    if (trigger > top) {
      box.classList.add("show-content");
    } else {
      box.classList.remove("show-content");
    }
  });
}

//TERMS

function disableSubmit() {
  document.getElementById("register_account").disabled = true;
}

function activateButton(element) {
  if (element.checked) {
    document.getElementById("register_account").disabled = false;
  } else {
    document.getElementById("register_account").disabled = true;
  }
}

//LOGIN

function validateLoginCellNumber() {
  var validateLoginCellNumberField =
    document.forms["login-form"]["cellNumberInput"].value;
  if (validateLoginCellNumberField == "") {
    alert("Please enter your cell number");
    return false;
  }
  else 
  {
    return true;
  }
}

function validateLoginPassword() {
  var validateLoginPasswordField =
    document.forms["login-form"]["passwordInput"].value;
  if (validateLoginPasswordField == "") {
    alert("Please enter your password");
    return false;
  }
  else 
  {
    return true;
  }
}
