import { Component } from "@angular/core";
import { UsersService } from "../users/users.service";
import { Router } from '@angular/router';



@Component({
  selector: "app-signin",
  templateUrl: "./signin.component.html",
  styleUrls: ["./signin.component.css"]
})
export class SigninComponent {
  mail: string = "";
  contrasena: string ="";

  constructor(public userService: UsersService,private router: Router) {}

  signin() {
    const user = {mail: this.mail, contrasena: this.contrasena};

    this.userService.signin(user).subscribe(data => {
      /**Para poner antes de los metodos despues del login
       * const token = this.cookieService.get('access_token');
        const headers = new HttpHeaders().set('Authorization', 'Bearer ' + token);
        this.http.get('your api endpoint', { headers: headers });)
       */

      this.userService.setToken(data.token);
      const id_usuario = data.id_usuario;
      this.router.navigate(['/usuario/' + id_usuario + '/eventos'])
      /*this.router.navigate(['/eventos'])*/
    });
    console.log(this.mail);
    console.log(this.contrasena);
  }
  login_route(){
    this.router.navigate(['/login']);
  }
}
