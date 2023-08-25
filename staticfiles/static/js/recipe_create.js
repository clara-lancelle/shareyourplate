var url = window.location.pathname;
if(url == '/recipe/create' || url.match(/\/recipe\/[\d]+\/edit/g)) {

    let addIngredientButton = document.querySelector("#add-ingredient-form")
    let addButton = document.querySelector("#add-form")
    document.querySelector("#id_form-INITIAL_FORMS").setAttribute('value', 0)
    document.querySelector("#id_ingredient_form-INITIAL_FORMS").setAttribute('value', 0)

    //add stage form
    addButton.addEventListener('click', () => {
        let stageForm = document.querySelectorAll(".stage_form")
        let container = document.querySelector("#form")
        let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
        
        let formNum = stageForm.length-1
        let newForm = stageForm[0].cloneNode(true)
        let formRegex = RegExp(`form-(\\d){1}-`,'g')
    
        formNum++
        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
        newForm.innerHTML = newForm.innerHTML.replace('disable', '')
        newForm.querySelector('.field-name').innerHTML =`Etape n° ${formNum+1}`
        container.insertBefore(newForm, addButton)
        totalForms.setAttribute('value', `${formNum+1}`)
    }) 

    // delete stage/ingredient form

        document.addEventListener('click', e => {
            if(e.target.checked) {
                if(!e.target.id.match(/[0]{1}/) && e.target.parentNode.parentNode.parentNode.className.match(/formset__item/)) {
                    e.target.parentNode.parentNode.parentNode.remove();
                    if(e.target.id.match(/ingredient/)) {
                        document.querySelector("#id_ingredient_form-TOTAL_FORMS").setAttribute('value', `${ingredientFormNum-1}`)
                    } else {
                        document.querySelector("#id_form-TOTAL_FORMS").setAttribute('value', `${formNum-1}`)
                    }
                }
            }    
        })


    //add ingredient form

    addIngredientButton.addEventListener('click', () => {
        let ingredientForm = document.querySelectorAll(".ingredient_form")
        let totalIngredientForms = document.querySelector("#id_ingredient_form-TOTAL_FORMS")
        let container = document.querySelector("#form")
        
        let ingredientFormNum = ingredientForm.length-1
        let newIngredientForm = ingredientForm[0].cloneNode(true)
        let formRegex = RegExp(`form-(\\d){1}-`,'g')
    
        ingredientFormNum++
        newIngredientForm.innerHTML = newIngredientForm.innerHTML.replace(formRegex, `form-${ingredientFormNum}-`)
        newIngredientForm.innerHTML = newIngredientForm.innerHTML.replace('disable', '')
        container.insertBefore(newIngredientForm, addIngredientButton)
        totalIngredientForms.setAttribute('value', `${ingredientFormNum+1}`)
    }) 
    
}
