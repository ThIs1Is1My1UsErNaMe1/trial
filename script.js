const container = document.querySelector(".container");
const addQuestionCard = document.getElementById("add-question-card");
const cardButton = document.getElementById("save-btn");
const question = document.getElementById("question");
const answer = document.getElementById("answer");
const errorMessage = document.getElementById("error");
const addQuestion = document.getElementById("add-flashcard");
const closeBtnQuestion = document.getElementById("close-btn-question");
const practice = document.getElementById("practice");
const practiceCard = document.getElementById("practice-card")
const closeBtnPractice = document.getElementById("close-btn-practice");
const titleText = document.getElementById("text");
const submitAnswerBtn = document.getElementById("submit-user-input");
const practiceFront = document.getElementById("practice-card-front")
const practiceInputCon = document.getElementById("practice-user-input")
const practiceUserGrade =document.getElementById("practice-user-grade")
let editBool = false;
//Add question when user clicks 'Add Flashcard' button
addQuestion.addEventListener("click", () => {
    titleText.classList.add("hide");
  container.classList.add("hide");
  question.value = "";
  answer.value = "";
  addQuestionCard.classList.remove("hide");
  data = {
    "question":question.value,
    "answer":answer.value,
  }
  jsonText.innerText = JSON.stringify(data)
});

practice.addEventListener("click", () => {
    titleText.classList.add("hide");
    container.classList.add("hide");
    practiceUserGrade.classList.add("hide")
    question.value = "";
    answer.value = "";
    practiceCard.classList.remove("hide");
    practiceInputCon.classList.remove("hide");
    data = {
      "question":question.value,
      "answer":answer.value,
    }
    jsonText.innerText = JSON.stringify(data)
  });
//Hide Create flashcard Card
closeBtnQuestion.addEventListener(
  "click",
  (hideQuestion = () => {
    container.classList.remove("hide");
    titleText.classList.remove("hide");
    addQuestionCard.classList.add("hide");
    if (editBool) {
      editBool = false;
      submitQuestion();
    }
  })
);
closeBtnPractice.addEventListener(
    "click",
    (hideQuestion = () => {
      container.classList.remove("hide");
      titleText.classList.remove("hide");
      practiceCard.classList.add("hide");
      practiceInputCon.classList.add("hide");
      practiceUserGrade.classList.add("hide");
      practiceFront.innerHTML="Flashcard Name";
      if (editBool) {
        editBool = false;
        submitQuestion();
      }
    })
  );
//Submit Question
cardButton.addEventListener(
  "click",
  (submitQuestion = () => {
    editBool = false;
    tempQuestion = question.value.trim();
    tempAnswer = answer.value.trim();
    if (!tempQuestion || !tempAnswer) {
      errorMessage.classList.remove("hide");
    } else {
      container.classList.remove("hide");
      errorMessage.classList.add("hide");
      viewlist();
      question.value = "";
      answer.value = "";
    }
  })
);
//Card Generate saving cards algorithm
function viewlist() {
  var listCard = document.getElementsByClassName("card-list-container");
  var div = document.createElement("div");
  div.classList.add("card");
  //Question
  div.innerHTML += `
  <p class="question-div">${question.value}</p>`;
  //Answer
  var displayAnswer = document.createElement("p");
  displayAnswer.classList.add("answer-div", "hide");
  displayAnswer.innerText = answer.value;
  //Link to show/hide answer
  var link = document.createElement("a");
  link.setAttribute("href", "#");
  link.setAttribute("class", "show-hide-btn");
  link.innerHTML = "Show/Hide";
  link.addEventListener("click", () => {
    displayAnswer.classList.toggle("hide");
  });
  div.appendChild(link);
  div.appendChild(displayAnswer);
  //Edit button
  let buttonsCon = document.createElement("div");
  buttonsCon.classList.add("buttons-con");
  var editButton = document.createElement("button");
  editButton.setAttribute("class", "edit");
  editButton.innerHTML = `<i class="fa-solid fa-pen-to-square"></i>`;
  editButton.addEventListener("click", () => {
    editBool = true;
    modifyElement(editButton, true);
    addQuestionCard.classList.remove("hide");
  });
  buttonsCon.appendChild(editButton);
  disableButtons(false);
  //Delete Button
  var deleteButton = document.createElement("button");
  deleteButton.setAttribute("class", "delete");
  deleteButton.innerHTML = `<i class="fa-solid fa-trash-can"></i>`;
  deleteButton.addEventListener("click", () => {
    modifyElement(deleteButton);
  });
  buttonsCon.appendChild(deleteButton);
  div.appendChild(buttonsCon);
  listCard[0].appendChild(div);
  hideQuestion();
}
//Modify Elements
const modifyElement = (element, edit = false) => {
  let parentDiv = element.parentElement.parentElement;
  let parentQuestion = parentDiv.querySelector(".question-div").innerText;
  if (edit) {
    let parentAns = parentDiv.querySelector(".answer-div").innerText;
    answer.value = parentAns;
    question.value = parentQuestion;
    disableButtons(true);
  }
  parentDiv.remove();
};
//Disable edit and delete buttons
const disableButtons = (value) => {
  let editButtons = document.getElementsByClassName("edit");
  Array.from(editButtons).forEach((element) => {
    element.disabled = value;
  });
};
submitAnswerBtn.addEventListener("click", () => {
    practiceFront.innerHTML = "Answer";
    practiceInputCon.classList.add("hide");
    practiceUserGrade.classList.remove("hide");

 
});
