package main
import(
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"gopkg.in/ini.v1"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func mkdirrr(){
	//creating the .git directory
	err := os.Mkdir(".git", 0755)
	check(err)

	//creating the hooks subd
	err := os.MkdirAll(".git/hooks", 0755)
	check(err)

	//creating the info subd
	err := os.MkdirAll(".git/info", 0755)
	check(err)

	//creating the objects subd
	err := os.MkdirAll(".git/objects", 0755)
	check(err)

	//creating the refs subd
	err := os.MkdirAll(".git/refs", 0755)
	check(err)

}

func create(){
	//creating the HEAD file (empty)
	file_name := "HEAD"
	file, err := os.Create(file_name)
	check(e)

	//creating the config file (empty)
	file_name := "config"
	file, err := os.Create(file_name)
	check(e)
	
	//creating the description file (empty)
	file_name := "description"
	file, err := os.Create(file_name)
	check(e)
}

func HEAD(){
	
}

func main(){

}