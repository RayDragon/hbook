class schoolManager
{
    constructor(){
        this.schoolList=[];
        if(!thisPage.logged){
            window.location = "../index.html";
        }
        pagefiller();

    }
    create_school(schoolName) {
        var self=this;
        var fun = (data, status)=>{
            self.schoolList.push(data.schName);
        }
        thisPage.requestServer("/school/create",{'type':'school', 'name':schoolName},fun, 'json');
    }


}
function log(data){
    console.log("LOG : "+data);
}
function pagefiller()
{   
    createSchool.get()
    $('#home').append(createSchool.card.card)
}
createSchool={
    card:'',
    inpschname:'',
    get:function(){
        this.card = new card("Create School", "", "");
        this.card.title.innerHTML = "Create School"
        this.card.body.innerHTML=""
        

    }
}
        