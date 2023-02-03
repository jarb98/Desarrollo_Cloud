import { Component, OnInit } from '@angular/core';
import { Evento } from './evento'
import { EventosService } from './eventos.service';
import { ActivatedRoute } from '@angular/router'


@Component({
  selector: 'app-eventos',
  templateUrl: './eventos.component.html',
  styleUrls: ['./eventos.component.css']
})
export class EventosComponent implements OnInit {

  eventos: Array<Evento> = [];
  id_usuario: number ;


  constructor(private eventosService: EventosService,private activatedRoute: ActivatedRoute) {
    this.id_usuario = +this.activatedRoute.snapshot.params['id_usuario']
  }
  getListaEventos(){

    this.eventosService.getListaEventos(this.id_usuario).subscribe(cs => {this.eventos = cs;});
  }


  ngOnInit() {
    this.id_usuario = this.activatedRoute.snapshot.params['id_usuario'];
    this.getListaEventos()
  }

}
