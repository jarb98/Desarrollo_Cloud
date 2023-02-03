import { RouterModule, Routes} from "@angular/router";
import { AppComponent } from "./app.component";
import { LoginComponent } from "./login/login.component";
import { SigninComponent } from "./signin/signin.component";
import { EventosComponent } from "./eventos/eventos.component";

const appRoutes:Routes= [
  { path: "", redirectTo:"login", pathMatch: "full" },
  { path: "login", component: LoginComponent, pathMatch: "full" },
  { path: "signin", component: SigninComponent, pathMatch: "full" },
  { path: "usuario/:id_usuario/eventos", component: EventosComponent, pathMatch: "full" }
];


export const routing = RouterModule.forRoot(appRoutes);
