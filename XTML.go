package main
import("encoding/json" "fmt" "log" "net/http" "string")

type User struct{
	Id int `json:"id"`
	UserName string `json:"username"`
	Email string `json:"email"`

}
var user=[]User{
	{Id:1,UserName:"Alise",Email:"kdsfjksd@fdsfsd.com"}
	{Id:2,UserName:"Lev",Email:"kdsfjksd@dsffdsfsd.com"}
}
func main(){
	http.HandleFunc("/user",getUser)
	http.HandleFunc("/user/create",createUser)
	log.Println("Server zapushen na http//localhost:8888")
	log.Fatal(http.ListenAndServe(":8080",nil))
}
func GetUser(w http.ResponseWriter, r*http.Request){
	w.Header().Set("Content-Type","aplication/json")
	json.newEncoder(w).Encode(users)
}
func createuser(w http.ResponseWriter,r * http.Request){
	if r.method!=http.MethodPost{
		http.Error(w,"Метод не поддерживается",http.StatusMethodNotAllowed)
		return
	}
	var newuser User
	err:=json.newDewcoder(r.body).Decode(&newuser) 
	if err!=null{
		http.Error(w."Неверный json ", http.StatusBadRequest)
		return
	}
	if strings.TrimSpace(newuser.UserName)==""||strings.TrimSpace(newuser.Email)==""{
		http.Error(w."Username and email is bad",http.StatusBadRequest)
		return
	}
	newId:=user[len(user)-1].ID+1
	newuser.Id=newId
	user-append(user,newuser)
	w.Header().Set("content-type","application/json")
	w.WriteHeader(http.StatusCreated)
	json.newEncoder(w).Encode(newuser)
}