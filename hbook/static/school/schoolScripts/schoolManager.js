/*sm = new class{
    constructor(fun=()=>{}){
        this.schoolList=[];
        if(!thisPage.logged){
            //window.location = "../index.html";
        }
        fun()
    }
    create_school(schoolName) {
        log("creating school")
        var self=this;
        var fun = (data, status)=>{
            self.schoolList.push(data.schName);
        }
        thisPage.requestServer("/school/create",{'type':'school', 'name':schoolName},fun, 'json');
    }


}*/
SchoolManager={
    schoolList:[],
    initialize:function(fun=()=>{}){
        if(!thisPage.logged){
            window.location = "../index.html";
        }
        fun()
    },
    create_school:function(schoolName, fun=function(){}) {
        log("creating school"+schoolName)
        var self=this;
        var func = (data, status)=>{
            if(data.status === 'success'){
                self.schoolList.push(data.data.School_Name);
            }
            else alert(data.status_message)
            log("called")
            fun()
        }
        thisPage.requestServer("/school/create",{'type':'school', 'name':schoolName},func, 'json');
    }
}
function log(data){
    console.log("LOG : "+data);
}

        