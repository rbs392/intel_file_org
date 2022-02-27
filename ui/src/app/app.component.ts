import { Component, ViewChild } from '@angular/core';
import { FormControl } from '@angular/forms';

enum IfoEntity {
  CATEGORY,
  FILE
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  myControl = new FormControl();

  public categories = [
    {
      type: IfoEntity.CATEGORY,
      title: 'July Salaries',
      description: 'Auto generated',
      team: 'HR Team',
      tags: 'HR, finance',
      actions: []
    },
    {
      type: IfoEntity.CATEGORY,
      title: 'Unit tests',
      description: 'Auto generated',
      team: 'Java Team',
      tags: 'Java, Development',
      actions: []
    },
    {
      type: IfoEntity.CATEGORY,
      title: 'Unit tests',
      description: 'Auto generated',
      team: 'Java Team',
      tags: 'Java, Development',
      actions: []
    },
    {
      type: IfoEntity.CATEGORY,
      title: 'Unit tests',
      description: 'Auto generated',
      team: 'Java Team',
      tags: 'Java, Development',
      actions: []
    },
    {
      type: IfoEntity.CATEGORY,
      title: 'Unit tests',
      description: 'Auto generated',
      team: 'Java Team',
      tags: 'Java, Development',
      actions: []
    },
    {
      type: IfoEntity.CATEGORY,
      title: 'Unit tests',
      description: 'Auto generated',
      team: 'Java Team',
      tags: 'Java, Development',
      actions: []
    }
  ];

  public handleFileInput(fileEvent: Event | null) {
    const fileList: FileList | [] = (fileEvent?.target as HTMLInputElement)?.files || [];
    const file = fileList[0];
    console.info(file);
  }
}
